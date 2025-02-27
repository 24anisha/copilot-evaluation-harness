/*
 * CFlash.cpp
 *
 *  Created on: 14.12.2009
 *      Author: gerstrong
 */

#include "CFlash.h"
#include <base/video/CVideoDriver.h>


CFlash::CFlash(Uint32 msecs, Uint8 speed,
               const GsColor color) :
    m_StartTime(gTimer.getTicks()),
    m_RunTime(msecs),
    m_Speed(speed)
{
    mFadeSurface.createCopy(gVideoDriver.getBlitSurface());
    mFadeSurface.fillRGBA(color);
}

CFlash::CFlash(Uint32 msecs, Uint8 speed, const GsColor color, Uint8 m_maxalpha) :
    m_StartTime(gTimer.getTicks()),
    m_RunTime(msecs),
    m_Speed(speed),
    m_Style(FADE_NORMAL),
    m_MaxAlpha(m_maxalpha)
{
    mFadeSurface.createCopy(gVideoDriver.getBlitSurface());
    mFadeSurface.fillRGBA(color);
}

// Process the flashing effect here
void CFlash::ponder(const float deltaT)
{
    Uint32 ElapsedTime = gTimer.getTicks() - m_StartTime;

    mFadeSurface.setAlpha(m_Alpha);

    if(m_FadeDir == FADE_IN)
    {
        if(m_Alpha+m_Speed > m_MaxAlpha) m_Alpha = m_MaxAlpha;
        else m_Alpha+=m_Speed;
    }
    if(m_FadeDir == FADE_OUT)
    {
        if(m_Alpha+m_Speed < 0) m_Alpha = 0;
        else m_Alpha-=m_Speed;
    }

    if(m_Style == FADE_PULSE)
    {
        if(m_Alpha == 255) m_FadeDir = FADE_OUT;
        else if(m_Alpha == 0) m_FadeDir = FADE_IN;
    }
    else if(m_Style == FADE_NORMAL)
    {
        if(ElapsedTime >= m_RunTime/2 ) m_FadeDir = FADE_OUT;
        if(m_FadeDir == FADE_OUT && m_Alpha == 0) mFinished = true;
    }

    // The developer set a time in the constructor. This effect will last for the given time.
    if(ElapsedTime >= m_RunTime)
        mFinished = true;
}

void CFlash::render()
{
    // Blit it and free temp surface
    GsWeakSurface blit(gVideoDriver.getBlitSurface());
    mFadeSurface.blitTo(blit);
    //blit.fillRGB(0xFF,0xFF,0xFF);
}